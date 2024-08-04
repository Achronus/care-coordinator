"use server";

import FetchClient from "@/lib/fetch-client";
import { AppointmentListData } from "@/types/api";
import { Doctor } from "@/types/common";

const fetch = new FetchClient(undefined, "api/retrieval");

export const getAppointments = async () => {
  const { data: appointments, error: appointmentError } =
    await fetch.get<AppointmentListData>("/appointment/list");
  return { appointments, appointmentError };
};

export const getDoctors = async () => {
  const { data: doctorsList, error: doctorError } = await fetch.get<Doctor[]>(
    "/doctor/list"
  );
  return { doctorsList, doctorError };
};
