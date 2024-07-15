import { ErrorMsg } from "@/types/api";

type DataResponse<T> = {
  data: T | null;
  isLoading: boolean;
  error: ErrorMsg | null;
};

function serverErrorMsg(): ErrorMsg {
  return {
    status: "Error",
    code: 500,
    response: "500_INTERNAL_SERVER_ERROR",
    message: "Internal server error occurred",
  };
}

export async function GetData<T>(url: string): Promise<DataResponse<T>> {
  let data: T | null = null;
  let isLoading = true;
  let error: ErrorMsg | null = null;

  try {
    const response = await fetch(`${process.env.FASTAPI_CONNECTION_URL}${url}`);
    const output = await response.json();

    if (!Object.hasOwn(output, "data")) {
      isLoading = false;
      error = output;
    } else {
      isLoading = false;
      data = output;
    }
  } catch (err) {
    console.error("Fetch error:", err);
    error = serverErrorMsg();
    isLoading = false;
  }

  return { data, isLoading, error };
}

export async function PostData<T>(
  url: string,
  postData: object
): Promise<DataResponse<T>> {
  let data: T | null = null;
  let error: ErrorMsg | null = null;
  let isLoading = true;

  try {
    const response = await fetch(
      `${process.env.FASTAPI_CONNECTION_URL}${url}`,
      {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json;charset=UTF-8",
        },
      }
    );
    const output = await response.json();

    if (!Object.hasOwn(output, "data")) {
      isLoading = false;
      error = output;
    } else {
      isLoading = false;
      data = output.data;
    }
  } catch (err) {
    console.error("Fetch error:", err);
    error = serverErrorMsg();
    isLoading = false;
  }

  return { data, isLoading, error };
}

export async function PostFormData<T>(
  url: string,
  formData: FormData
): Promise<DataResponse<T>> {
  let data: T | null = null;
  let error: ErrorMsg | null = null;
  let isLoading = true;

  try {
    const response = await fetch(
      `${process.env.FASTAPI_CONNECTION_URL}${url}`,
      {
        method: "POST",
        body: formData,
      }
    );
    const output = await response.json();

    if (!Object.hasOwn(output, "data")) {
      isLoading = false;
      error = output;
    } else {
      isLoading = false;
      data = output.data;
    }
  } catch (err) {
    console.error("Fetch error:", err);
    error = serverErrorMsg();
    isLoading = false;
  }

  return { data, isLoading, error };
}
