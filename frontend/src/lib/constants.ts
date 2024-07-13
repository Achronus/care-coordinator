import { Gender } from "@/types/enums";

export const Logo: ImageType = {
  src: "/logo.svg",
  height: 1000,
  width: 1000,
  alt: "Care Coordinator logo",
};

export const DisplayImg: ImageType = {
  src: "/onboarding.png",
  height: 1000,
  width: 1000,
  alt: "Onboarding",
  className: "max-w-[55%]",
};

export const RegisterImg: ImageType = {
  src: "/register.png",
  height: 1000,
  width: 1000,
  alt: "Register",
  className: "max-w-[390px]",
};

export const RegistrationFormDefaults = {
  name: "",
  email: "",
  phone: "",
  userId: "",
  birthDate: new Date(Date.now()),
  gender: "Male" as Gender,
  address: "",
  occupation: "",
  emergencyContactName: "",
  emergencyContactNumber: "",
  primaryPhysician: "",
  insuranceProvider: "",
  insurancePolicyNumber: "",
  allergies: "",
  currentMedication: "",
  familyMedicalHistory: "",
  pastMedicalHistory: "",
  identificationType: undefined,
  identificationNumber: "",
  identificationDocument: undefined,
  treatmentConsent: false,
  disclosureConsent: false,
  privacyConsent: false,
};
