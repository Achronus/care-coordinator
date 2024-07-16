"use client";

import AppointmentForm from "@/forms/AppointmentForm";
import FormLayout from "@/layouts/Form";
import { AppointmentImg, Logo } from "@/lib/constants";
import { AppointmentType } from "@/types/enums";

import { useSearchParams } from "next/navigation";

const NewAppointment = ({ params }: { params: { userId: string } }) => {
  const searchParams = useSearchParams();

  const patientId = searchParams.get("patientId") ?? "";

  return (
    <main className="flex h-screen max-h-screen">
      <FormLayout
        containerStyles="max-w-[860px] flex-1 justify-between"
        logo={Logo}
        displayImg={AppointmentImg}
      >
        <AppointmentForm
          type={AppointmentType.CREATE}
          userId={params.userId}
          patientId={patientId}
        />
      </FormLayout>
    </main>
  );
};

export default NewAppointment;
