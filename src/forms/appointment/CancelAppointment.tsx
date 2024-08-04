"use client";

import DynamicFormField from "@/components/DynamicFormField";
import ErrorPanel from "@/components/ErrorPanel";
import SubmitButton from "@/components/SubmitButton";
import { Form } from "@/components/ui/form";
import { CancelAppointmentSchema } from "@/lib/validation";

import { ErrorMsg, SingleAppointmentItem } from "@/types/api";
import { FormFieldType } from "@/types/enums";
import { CancellationFormType } from "@/types/forms";

import { zodResolver } from "@hookform/resolvers/zod";
import { useRouter, useSearchParams } from "next/navigation";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";

type CancelAppointmentProps = {
  appointment: SingleAppointmentItem;
};

const CancelAppointment = ({ appointment }: CancelAppointmentProps) => {
  const [type, setType] = useState("cancel");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<ErrorMsg | null>(null);
  const [formData, setFormData] = useState<CancellationFormType>({
    cancellationReason: appointment ? appointment.cancellationReason : "",
  });
  const router = useRouter();
  const searchParams = useSearchParams();

  const appointmentId = searchParams.get("appointmentId") ?? "";

  const form = useForm<z.infer<typeof CancelAppointmentSchema>>({
    resolver: zodResolver(CancelAppointmentSchema),
    defaultValues: formData,
  });

  const onSubmit = async (
    formValues: z.infer<typeof CancelAppointmentSchema>
  ) => {
    setIsLoading(true);
    router.push("/admin?success=true");
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6 flex-1">
        <DynamicFormField
          fieldType={FormFieldType.TEXTAREA}
          control={form.control}
          name="cancellationReason"
          label="Reason For Cancellation"
          placeholder="Enter reason for cancellation"
        />

        <SubmitButton isLoading={isLoading} className="shad-danger-btn w-full">
          Cancel Appointment
        </SubmitButton>

        {error && <ErrorPanel error={error} />}
      </form>
    </Form>
  );
};

export default CancelAppointment;
