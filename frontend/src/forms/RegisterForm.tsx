"use client";

import DynamicFormField from "@/components/DynamicFormField";
import ErrorPanel from "@/components/ErrorPanel";
import SubmitButton from "@/components/SubmitButton";
import { Form } from "@/components/ui/form";
import { PostData } from "@/lib/retrieval";

import { UserFormValidation } from "@/lib/validation";
import { ErrorMsg, User } from "@/types/api";
import { FormFieldType } from "@/types/enums";

import { zodResolver } from "@hookform/resolvers/zod";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";

const RegistrationForm = {
  name: "",
  email: "",
  phone: "",
};

const RegisterForm = ({ user }: { user: User }) => {
  const router = useRouter();

  const [formSubmitLoading, setFormSubmitLoading] = useState(false);
  const [formData, setFormData] = useState(RegistrationForm);
  const [formError, setFormError] = useState<ErrorMsg | null>(null);

  const form = useForm<z.infer<typeof UserFormValidation>>({
    resolver: zodResolver(UserFormValidation),
    defaultValues: formData,
  });

  const onSubmit = async ({
    name,
    email,
    phone,
  }: z.infer<typeof UserFormValidation>) => {
    setFormSubmitLoading(true);

    const { data: user, error } = await PostData<User>("<TBC>", {
      name,
      email,
      phone,
    });

    if (user) {
      // router.push(`<TBC>>`);
    } else {
      setFormData({ name, email, phone });
      setFormSubmitLoading(false);
      setFormError(error);
    }
  };

  return (
    <Form {...form}>
      <form
        method="POST"
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-12 flex-1"
      >
        <section className="space-y-4">
          <h1 className="header">Getting Setup</h1>
          <p className="text-dark-700">Let us know more about you!</p>
        </section>

        <section className="space-y-4">
          <div className="mb-9 space-y-1">
            <h2 className="sub-header">Personal Information</h2>
          </div>
          <DynamicFormField
            fieldType={FormFieldType.INPUT}
            control={form.control}
            name="name"
            label="Full Name"
            placeholder="ex: Adam"
          />

          <div className="two-columns">
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
          </div>

          <div className="two-columns">
            <DynamicFormField
              fieldType={FormFieldType.DATE_PICKER}
              control={form.control}
              name="birthDate"
              label="Date of Birth"
            />

            <DynamicFormField
              fieldType={FormFieldType.SKELETON}
              control={form.control}
              name="gender"
              label="Gender"
            />
          </div>
        </section>

        <SubmitButton isLoading={formSubmitLoading}>
          Submit and Continue
        </SubmitButton>

        {formError && <ErrorPanel error={formError} />}
      </form>
    </Form>
  );
};

export default RegisterForm;
