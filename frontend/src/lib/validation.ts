import { z } from "zod";
import validator from "validator";

export const UserFormValidation = z.object({
  name: z
    .string()
    .min(2, {
      message: "Name must be at least 2 characters.",
    })
    .max(50, "Name cannot exceed 50 characters."),
  email: z.string().email("Invalid email address."),
  phone: z
    .string()
    .refine(
      (phone) => validator.isMobilePhone(phone, "any", { strictMode: true }),
      {
        message: "Invalid phone number.",
      }
    ),
});
