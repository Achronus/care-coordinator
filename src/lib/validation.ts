import { z } from "zod";
import { Gender, IdentificationTypes } from "@/types/enums";

export const UserFormValidation = z.object({
  name: z.string().max(50, "Name cannot exceed 50 characters.").optional(),
  email: z.string().optional(),
  phone: z.string().optional(),
});

export const RegistrationFormValidation = z.object({
  name: z.string().optional(),
  email: z.string().optional(),
  phone: z.string().optional(),
  birthDate: z.coerce.date().optional(),
  gender: z.nativeEnum(Gender).optional(),
  address: z.string().optional(),
  occupation: z.string().optional(),
  emergencyContactName: z.string().optional(),
  emergencyContactNumber: z.string().optional(),
  primaryPhysician: z.string().optional(),
  insuranceProvider: z.string().optional(),
  insurancePolicyNumber: z.string().optional(),
  allergies: z.string().optional(),
  currentMedication: z.string().optional(),
  familyMedicalHistory: z.string().optional(),
  pastMedicalHistory: z.string().optional(),
  identificationType: z
    .nativeEnum(IdentificationTypes, {
      message: "A type must be selected",
    })
    .optional(),
  identificationNumber: z.string().optional(),
  identificationDocument: z
    .custom<File[]>((val) => val, "An identification document is required")
    .optional(),
  treatmentConsent: z.boolean().default(false).optional(),
  disclosureConsent: z.boolean().default(false).optional(),
  privacyConsent: z.boolean().default(false).optional(),
});

export const CreateAppointmentSchema = z.object({
  primaryPhysician: z.string().min(2, "Please select a doctor").optional(),
  schedule: z.coerce.date().optional(),
  reason: z
    .string()
    .max(300, "Reason must be at most 300 characters")
    .optional(),
  notes: z
    .string()
    .max(300, "Reason must be at most 300 characters")
    .optional(),
  cancellationReason: z.string().optional(),
});

export const ScheduleAppointmentSchema = z.object({
  primaryPhysician: z.string().min(2, "Please select a doctor"),
  reason: z
    .string()
    .max(300, "Reasons must be at most 300 characters")
    .optional(),
  notes: z
    .string()
    .max(300, "Reason must be at most 300 characters")
    .optional(),
  schedule: z.coerce.date(),
});

export const CancelAppointmentSchema = z.object({
  cancellationReason: z
    .string()
    .max(300, "Reason must be at most 300 characters")
    .optional(),
});
