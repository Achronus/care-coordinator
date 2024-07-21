"use client";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";

import AppointmentForm from "@/forms/appointment";
import { cn, title } from "@/lib/utils";
import { SingleAppointmentItem } from "@/types/api";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

type AppointmentModalProps = {
  type: "schedule" | "cancel";
  appointment?: SingleAppointmentItem;
  description: string;
};

const AppointmentModal = ({
  type,
  appointment,
  description,
}: AppointmentModalProps) => {
  const router = useRouter();
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (!open) {
      router.push("/admin");
    } else {
      router.push(`/admin?appointmentId=${appointment!.id}`);
    }
  }, [open]);

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button
          variant="ghost"
          className={cn("capitalize", {
            "text-green-500": type === "schedule",
            "text-white": type === "cancel",
          })}
        >
          {type}
        </Button>
      </DialogTrigger>
      <DialogContent className="shad-dialog sm:max-w-md">
        <DialogHeader className="mb-4 space-y-3">
          <DialogTitle className="capitalize">
            {title(type)} Appointment
          </DialogTitle>
          <DialogDescription>{description}</DialogDescription>
        </DialogHeader>

        <AppointmentForm type={type} />
      </DialogContent>
    </Dialog>
  );
};

export default AppointmentModal;
