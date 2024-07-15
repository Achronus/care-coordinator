import { CreateUser } from "./api";
import { Gender, IdentificationTypes, Status } from "./enums";

export type PatientDetails = CreateUser & {
  birthDate?: Date;
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
  identificationNumber: string;
  treatmentConsent: boolean;
  disclosureConsent: boolean;
  privacyConsent: boolean;
};

export type PatientDetailsForm = PatientDetails & {
  identificationDocument?: File[];
};

export type Appointment = {
  patient: Patient;
  schedule: Date;
  status: Status;
  primaryPhysician: string;
  reason: string;
  notes?: string;
  userId: string;
  cancellationReason: string | null;
};

export type AppointmentForm = {
  primaryPhysician?: string;
  reason?: string;
  notes?: string;
  schedule?: Date;
  cancellationReason?: string;
};
