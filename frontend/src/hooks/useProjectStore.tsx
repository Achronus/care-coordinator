import {
  AppointmentStore,
  createAppointmentStore,
} from "@/stores/AppointmentStore";
import { DoctorStore, createDoctorStore } from "@/stores/DoctorStore";
import { PatientStore, createPatientStore } from "@/stores/PatientStore";

import { create } from "zustand";

export type AppState = DoctorStore & AppointmentStore & PatientStore;

export const useProjectStore = create<AppState>((set, get, store) => ({
  ...createDoctorStore(set, get, store),
  ...createAppointmentStore(set, get, store),
  ...createPatientStore(set, get, store),
}));
