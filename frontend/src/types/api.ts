import { Appointment } from "./appwrite.types";
import { Gender, IdentificationTypes, Status } from "./enums";

export type FileData = {
  filename: string;
  type: string;
  size: number;
  data: Uint8Array;
};

export type CreateUserParams = {
  name: string;
  email: string;
  phone: string;
};

export type User = CreateUserParams & {
  userID: string;
};

export type PatientDetails = CreateUserParams & {
  birthDate: Date | string;
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
  identificationType?: IdentificationTypes;
  identificationNumber?: string;
  treatmentConsent: boolean;
  disclosureConsent: boolean;
  privacyConsent: boolean;
};

export type RegisterPatientParams = PatientDetails & {
  identificationDocument?: File[];
};

export type PatientDetailsAPI = PatientDetails & {
  userId: string;
  identificationDocument?: FileData;
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

export type PhysicianList = {
  status: string;
  code: number;
  response: string;
  data: Avatar[];
  headers: null;
};
