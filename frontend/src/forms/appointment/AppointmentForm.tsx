"use client";

import CancelAppointment from "./CancelAppointment";
import ScheduleAppointment from "./ScheduleAppointment";

type AppointmentFormProps = {
  type: "cancel" | "schedule";
};

const AppointmentForm = ({ type }: AppointmentFormProps) => {
  return (
    <>
      {type === "cancel" ? (
        <CancelAppointment />
      ) : (
        type === "schedule" && <ScheduleAppointment />
      )}
    </>
  );
};

export default AppointmentForm;
