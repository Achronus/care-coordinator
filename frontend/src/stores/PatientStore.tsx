import FetchClient from "@/lib/fetch-client";
import { APIDataId, CreatePatient, ErrorMsg } from "@/types/api";

import { StateCreator } from "zustand";

type Error = ErrorMsg | null;

export type PatientStore = {
  patient: APIDataId | null;
  fileDetails: APIDataId | null;
  patientsLoading: boolean;
  patientError: Error;
  addPatient: (patient: CreatePatient) => Promise<void>;
  uploadFile: (file: FormData) => Promise<void>;
};

const fetch = new FetchClient(undefined, "api/patient");

const APIAction = <T, Params = void>(
  apiCall: (
    params: Params
  ) => Promise<{ data: T | null; isLoading: boolean; error: Error }>,
  setState: (state: Partial<PatientStore>) => void,
  stateKey: keyof PatientStore
) => {
  return async (params: Params) => {
    setState({ patientsLoading: true });
    const { data, isLoading, error } = await apiCall(params);
    setState({
      [stateKey]: data,
      patientsLoading: isLoading,
      patientError: error,
    });
  };
};

export const createPatientStore: StateCreator<PatientStore> = (set) => ({
  patient: null,
  fileDetails: null,
  patientsLoading: true,
  patientError: null,
  addPatient: APIAction(
    (patient: CreatePatient) => fetch.post<APIDataId>("/register", patient),
    set,
    "patient"
  ),
  uploadFile: APIAction(
    (file: FormData) => fetch.post<APIDataId>(`/upload`, file),
    set,
    "fileDetails"
  ),
});
