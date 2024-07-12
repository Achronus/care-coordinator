import { GetData } from "@/lib/retrieval";
import { ErrorMsg } from "@/types/api";
import { useCallback, useEffect, useState } from "react";

export default function useGetApiData<T>(
  url: string,
  dependencies: any[] = []
) {
  const [data, setData] = useState<T | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<ErrorMsg | null>(null);

  const callbackMemoized = useCallback(async () => {
    const { data, isLoading, error } = await GetData<T>(url);
    setError(error);
    setData(data);
    setIsLoading(isLoading);
  }, [url].concat(dependencies));

  useEffect(() => {
    callbackMemoized();
  }, [callbackMemoized]);

  return { data, isLoading, error };
}
