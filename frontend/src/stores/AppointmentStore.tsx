import FetchClient from "@/lib/fetch-client";
import {
  APIDataId,
  AppointmentListData,
  AppointmentSuccessDetails,
  CancelAppointmentParams,
  CreateAppointmentParams,
  ErrorMsg,
  ScheduleAppointmentParams,
} from "@/types/api";

import { StateCreator } from "zustand";

type Error = ErrorMsg | null;

export type AppointmentStore = {
  appointments: AppointmentListData | null;
  appointment: AppointmentSuccessDetails | null;
  appointmentId: APIDataId | null;
  appointmentsLoading: boolean;
  appointmentError: Error;
  getAppointments: () => Promise<void>;
  getSuccessDetails: (id: string) => Promise<void>;
  addAppointment: (appointment: CreateAppointmentParams) => Promise<void>;
  cancelAppointment: (appointment: CancelAppointmentParams) => Promise<void>;
  scheduleAppointment: (
    appointment: ScheduleAppointmentParams
  ) => Promise<void>;
};

const fetch = new FetchClient(undefined, "api/appointment");

const APIAction = <T, Params = void>(
  apiCall: (
    params: Params
  ) => Promise<{ data: T | null; isLoading: boolean; error: Error }>,
  setState: (state: Partial<AppointmentStore>) => void,
  stateKey: keyof AppointmentStore,
  afterSuccess?: (data: T) => void
) => {
  return async (params: Params) => {
    setState({ appointmentsLoading: true });
    const { data, isLoading, error } = await apiCall(params);
    setState({
      [stateKey]: data,
      appointmentsLoading: isLoading,
      appointmentError: error,
    });

    if (data && afterSuccess) {
      afterSuccess(data);
    }
  };
};

export const createAppointmentStore: StateCreator<AppointmentStore> = (
  set,
  get
) => ({
  appointments: null,
  appointment: null,
  appointmentId: null,
  appointmentsLoading: true,
  appointmentError: null,
  getAppointments: APIAction(
    () => fetch.get<AppointmentListData>("/list"),
    set,
    "appointments"
  ),
  getSuccessDetails: APIAction(
    (id: string) => fetch.get<AppointmentSuccessDetails>(`/${id}/success`),
    set,
    "appointment"
  ),
  addAppointment: APIAction(
    (appointment: CreateAppointmentParams) =>
      fetch.post<APIDataId>("/create", appointment),
    set,
    "appointmentId",
    async () => {
      await get().getAppointments();
    }
  ),
  cancelAppointment: APIAction(
    (appointment: CancelAppointmentParams) =>
      fetch.patch<APIDataId>("/cancel", appointment),
    set,
    "appointmentId",
    async () => {
      await get().getAppointments();
    }
  ),
  scheduleAppointment: APIAction(
    (appointment: ScheduleAppointmentParams) =>
      fetch.patch<APIDataId>("/schedule", appointment),
    set,
    "appointmentId",
    async () => {
      await get().getAppointments();
    }
  ),
});
