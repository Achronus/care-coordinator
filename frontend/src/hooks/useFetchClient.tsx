import { useCallback, useState } from "react";

import FetchClient from "@/lib/fetch-client";
import { ErrorMsg } from "@/types/api";

/**
 * Custom React hook for performing HTTP requests using the `FetchClient` class.
 *
 * @param {string} rootUrl - [rootUrl=process.env.FASTAPI_CONNECTION_URL] - The base URL for the API requests. This is used by the `FetchClient` to construct full URLs.
 *  The URL must end with a '/' to ensure proper URL construction for API requests.
 *  If not provided, it defaults to `process.env.FASTAPI_CONNECTION_URL`.
 *
 * @template T - The type of the response data that is expected from the API requests.
 *
 * @returns {Output} An object containing the state of the request and methods for performing HTTP operations: `{data, isLoading, error, fetch}`.
 *
 *
 * @typedef {Object} Output
 * @property {T|null} data - The data returned from the API response, or `null` if no data is available.
 * @property {boolean} isLoading - A boolean indicating if the request is currently in progress.
 * @property {ErrorMsg|null} error - An error message if the request fails, or `null` if no error occurred.
 * @property {Object} fetch - an object with common API request methods: `get`, `post`, `put`, `patch`, and `delete`.
 *
 * @typedef {Object} ErrorMsg
 * @property {string} status - The HTTP status of the error response.
 * @property {number} code - The error code associated with the error.
 * @property {string} response - The raw response body from the server.
 * @property {string} message - A descriptive error message.
 *
 * @example
 * const { data: appointmentData, isLoading, error, fetch } = useFetchClient<AppointmentListData>();
 *
 * useEffect(() => {
 *  fetch.get("api/appointment/list");
 * }, [fetch]);
 */
export default function useFetchClient<T>(rootUrl?: string) {
  const [data, setData] = useState<T | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<ErrorMsg | null>(null);

  const client = new FetchClient(rootUrl);

  const request = useCallback(
    async (
      method: "get" | "post" | "patch" | "put" | "delete",
      url: string,
      data?: object | FormData,
      headers?: HeadersInit
    ) => {
      const {
        data: responseData,
        isLoading,
        error,
        // @ts-ignore
      } = await client[method]<T>(url, data, headers);

      setData(responseData);
      setIsLoading(isLoading);
      setError(error);
    },
    []
  );

  const fetch = {
    get: useCallback(
      (url: string, headers?: HeadersInit) =>
        request("get", url, undefined, headers),
      [request]
    ),
    post: useCallback(
      (url: string, data: object | FormData, headers?: HeadersInit) =>
        request("post", url, data, headers),
      [request]
    ),
    put: useCallback(
      (url: string, data: object, headers?: HeadersInit) =>
        request("put", url, data, headers),
      [request]
    ),
    patch: useCallback(
      (url: string, data: object, headers?: HeadersInit) =>
        request("put", url, data, headers),
      [request]
    ),
    delete: useCallback(
      (url: string, headers?: HeadersInit) =>
        request("delete", url, undefined, headers),
      [request]
    ),
  };

  return { data, isLoading, error, fetch };
}
