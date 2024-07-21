import { useCallback, useEffect, useMemo, useState } from "react";

import FetchClient from "@/lib/fetch-client";
import { ErrorMsg } from "@/types/api";

export default function useFetchData<T>(
  url: string,
  dependencies: any[] = [],
  headers?: HeadersInit,
  rootUrl?: string
) {
  const [data, setData] = useState<T | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<ErrorMsg | null>(null);

  const fetch = useMemo(() => new FetchClient(rootUrl), [rootUrl]);

  const callbackMemoized = useCallback(async () => {
    const { data, isLoading, error } = await fetch.get<T>(url, headers);
    setError(error);
    setData(data);
    setIsLoading(isLoading);
  }, [url, headers].concat(dependencies));

  useEffect(() => {
    callbackMemoized();
  }, [callbackMemoized]);

  return { data, isLoading, error };
}
