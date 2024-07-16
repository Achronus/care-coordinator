"use client";

import DynamicFormField from "@/components/DynamicFormField";
import ErrorPanel from "@/components/ErrorPanel";
import { Loading } from "@/components/Loading";
import SubmitButton from "@/components/SubmitButton";
import { Form } from "@/components/ui/form";
import { SelectItem } from "@/components/ui/select";
import useGetApiData from "@/hooks/useGetApiData";
import {
  AppointmentFormDefaults,
  AppointmentTypeDetails,
} from "@/lib/constants";
import { PostData } from "@/lib/retrieval";
import { title } from "@/lib/utils";
import { getAppointmentSchema } from "@/lib/validation";

import {
  APIDataId,
  CreateAppointmentParams,
  ErrorMsg,
  PhysicianList,
} from "@/types/api";
import { AppointmentType, FormFieldType } from "@/types/enums";
import { AppointmentFormType } from "@/types/forms";

import { zodResolver } from "@hookform/resolvers/zod";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";

type AppointmentFormProps = {
  type: AppointmentType;
  userId: string;
  patientId: string;
};

const AppointmentForm = ({ type, userId, patientId }: AppointmentFormProps) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<ErrorMsg | null>(null);
  const [formData, setFormData] = useState<AppointmentFormType>(
    AppointmentFormDefaults
  );
  const router = useRouter();

  const AppointmentFormValidation = getAppointmentSchema(type);

  const { data: doctors, isLoading: doctorsLoading } =
    useGetApiData<PhysicianList>("api/doctor/list");

  const form = useForm<z.infer<typeof AppointmentFormValidation>>({
    resolver: zodResolver(AppointmentFormValidation),
    defaultValues: formData,
  });

  const onSubmit = async (
    formValues: z.infer<typeof AppointmentFormValidation>
  ) => {
    setIsLoading(true);
    try {
      const details = AppointmentTypeDetails.find((item) => item.type === type);

      if (details && type === "create" && patientId) {
        const appointmentData: CreateAppointmentParams = {
          userId,
          patient: patientId,
          primaryPhysician: formValues.primaryPhysician,
          schedule: new Date(formValues.schedule),
          reason: formValues.reason!,
          status: details.status,
          notes: formValues.notes,
        };

        const { data: appointment, error } = await PostData<APIDataId>(
          "api/appointment/create",
          appointmentData
        );

        if (appointment) {
          router.push(
            `/patients/${userId}/new-appointment/success?appointmentId=${appointment.id}`
          );
        } else {
          setFormData(formValues);
          setIsLoading(false);
          setError(error);
        }
      }
    } catch (error: any) {
      console.log(error);
      setFormData(formValues);
      setIsLoading(false);
      setError({
        status: "error",
        code: 500,
        response: "500_INTERNAL_SERVER_ERROR",
        message: error.message,
      });
    }
  };

  return (
    <Form {...form}>
      <form
        method="POST"
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-6 flex-1"
      >
        <section className="mb-12 space-y-4">
          <h1 className="header">Last Step! 🚀</h1>
          <p className="text-dark-700">Request a new appointment in seconds.</p>
        </section>

        {type !== "cancel" && (
          <>
            <DynamicFormField
              fieldType={FormFieldType.SELECT}
              control={form.control}
              name="primaryPhysician"
              label="Doctor"
              placeholder="Select a doctor"
            >
              {doctorsLoading && !doctors ? (
                <SelectItem value="loading">
                  <Loading width={10} height={10} />
                </SelectItem>
              ) : (
                doctors &&
                doctors.data.map((doctor: Avatar) => (
                  <SelectItem key={doctor.name} value={doctor.name}>
                    <div className="flex cursor-pointer items-center gap-2">
                      <Image
                        src={doctor.avatarIcon}
                        width={32}
                        height={32}
                        alt={doctor.name}
                        className="rounded-full border border-dark-500"
                      />
                      <p>{doctor.name}</p>
                    </div>
                  </SelectItem>
                ))
              )}
            </DynamicFormField>

            <div className="flex flex-col gap-6 xl:flex-row">
              <DynamicFormField
                fieldType={FormFieldType.TEXTAREA}
                control={form.control}
                name="reason"
                label="Reason For Appointment"
                placeholder="The reason for your appointment"
              />

              <DynamicFormField
                fieldType={FormFieldType.TEXTAREA}
                control={form.control}
                name="notes"
                label="Notes"
                placeholder="Additional information we need to know"
              />
            </div>

            <DynamicFormField
              fieldType={FormFieldType.DATE_PICKER}
              control={form.control}
              name="schedule"
              label="Expected Appointment Date"
              placeholder="Select your appointment date and time"
              showTimeSelect
              dateFormat="dd/MM/yyyy, hh:mm:aa"
            />
          </>
        )}

        {type === "cancel" && (
          <DynamicFormField
            fieldType={FormFieldType.TEXTAREA}
            control={form.control}
            name="cancellationReason"
            label="Reason For Cancellation"
            placeholder="Enter reason for cancellation"
          />
        )}

        <SubmitButton
          isLoading={isLoading}
          className={`${
            type === "cancel" ? "shad-danger-btn" : "shad-primary-btn"
          } w-full`}
        >
          {`${title(type)} Appointment`}
        </SubmitButton>

        {error && <ErrorPanel error={error} />}
      </form>
    </Form>
  );
};

export default AppointmentForm;
