"use client";

import DynamicFormField from "@/components/DynamicFormField";
import SubmitButton from "@/components/SubmitButton";
import { Form } from "@/components/ui/form";

import { UserFormValidation } from "@/lib/validation";
import { FormFieldType } from "@/types/enums";

import { zodResolver } from "@hookform/resolvers/zod";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";

const PatientForm = () => {
  const [isLoading, setIsLoading] = useState(false);

  const form = useForm<z.infer<typeof UserFormValidation>>({
    resolver: zodResolver(UserFormValidation),
    defaultValues: {
      name: "",
      email: "",
      phone: "",
    },
  });

  function onSubmit(values: z.infer<typeof UserFormValidation>) {
    console.log(values);
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6 flex-1">
        <section className="mb-12 space-y-4">
          <h1 className="header">Get Started</h1>
          <p className="text-dark-700">Schedule your first appointment.</p>
        </section>

        <DynamicFormField
          fieldType={FormFieldType.INPUT}
          control={form.control}
          name="name"
          label="Full name"
          placeholder="John Doe"
          iconSrc="/icons/user.svg"
          iconAlt="user"
        />

        <DynamicFormField
          fieldType={FormFieldType.INPUT}
          control={form.control}
          name="email"
          label="Email"
          placeholder="johndoe@youremail.com"
          iconSrc="/icons/email.svg"
          iconAlt="email"
        />

        <DynamicFormField
          fieldType={FormFieldType.PHONE_INPUT}
          control={form.control}
          name="phone"
          label="Phone number"
          placeholder="(555) 123-4567"
        />

        <SubmitButton isLoading={isLoading}>Get Started</SubmitButton>
      </form>
    </Form>
  );
};

export default PatientForm;
