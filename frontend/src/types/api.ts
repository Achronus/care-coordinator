import { PatientDetails } from "./forms";

export type CreateUser = {
  name: string;
  email: string;
  phone: string;
};

export type User = CreateUser & {
  userID: string;
};

export type CreatePatient = PatientDetails & {
  userId: string;
  primaryPhysician: string;
  identificationDocumentId?: string;
};

export type APIDataId = {
  id: string;
};

export type CreateAppointmentParams = {
  userId: string;
  patient: string;
  primaryPhysician: string;
  schedule: Date;
  reason: string;
  status: string;
  notes?: string;
};

export type UpdateAppointmentParams = {
  appointmentId: string;
  userId: string;
  type: string;
};

export type ErrorMsg = {
  status: string;
  code: number;
  response: string;
  message: string;
};

export type UserResponse = {
  status: string;
  code: number;
  response: string;
  data: User;
  headers: null;
};

export type AppointmentSuccessDetails = {
  id: string;
  schedule: string;
  doctor: Doctor;
};
