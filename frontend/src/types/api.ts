import { Appointment } from "./appwrite.types";
import { Gender, Status } from "./enums";

export type CreateUserParams = {
  name: string;
  email: string;
  phone: string;
};

export type User = CreateUserParams & {
  userID: string;
};

export type RegisterUserParams = CreateUserParams & {
  userId: string;
  birthDate: Date;
  gender: Gender;
  address: string;
  occupation: string;
  emergencyContactName: string;
  emergencyContactNumber: string;
  primaryPhysician: string;
  insuranceProvider: string;
  insurancePolicyNumber: string;
  allergies?: string;
  currentMedication?: string;
  familyMedicalHistory?: string;
  pastMedicalHistory?: string;
  identificationType?: string;
  identificationNumber?: string;
  identificationDocument?: FormData;
  privacyConsent: boolean;
};

export type CreateAppointmentParams = {
  userId: string;
  patient: string;
  primaryPhysician: string;
  reason: string;
  schedule: Date;
  status: Status;
  note?: string;
};

export type UpdateAppointmentParams = {
  appointmentId: string;
  userId: string;
  appointment: Appointment;
  type: string;
};

export type ErrorMsg = {
  status: string;
  code: number;
  response: string;
  message: string;
};
