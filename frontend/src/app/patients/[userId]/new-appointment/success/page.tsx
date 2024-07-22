"use client";

import { Loading } from "@/components/Loading";
import { Button } from "@/components/ui/button";
import { useProjectStore } from "@/hooks/useProjectStore";
import { cn, formatDateTime } from "@/lib/utils";

import Image from "next/image";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useEffect } from "react";

const Success = ({ params }: { params: { userId: string } }) => {
  const searchParams = useSearchParams();
  const appointmentId = searchParams.get("appointmentId") ?? "";

  const { appointment, appointmentsLoading, getSuccessDetails } =
    useProjectStore();

  useEffect(() => {
    getSuccessDetails(appointmentId);
  }, [getSuccessDetails]);

  return (
    <main className="flex flex-col h-screen max-h-screen px-[5%]">
      <div className="success-img">
        <Link href="/">
          <Image
            src="/logo.svg"
            width={1000}
            height={1000}
            alt="logo"
            className="h-10 w-fit"
          />
        </Link>

        <section className="flex flex-col items-center">
          <Image
            src="/success.gif"
            width={280}
            height={300}
            alt="success"
            className="mb-4"
          />
          <h2 className="header mb-6 max-w-[600px] text-center !leading-snug">
            Your <span className="text-green-500">appointment request</span> has
            been successfully submitted!
          </h2>
          <p>{`We'll`} be in touch shortly to confirm.</p>
        </section>

        <section className="request-details">
          {appointmentsLoading ? (
            <Loading />
          ) : (
            appointment && (
              <>
                <p>Requested appointment details:</p>
                <div className="flex items-center gap-3">
                  <Image
                    src={appointment.doctor.avatarIcon}
                    width={100}
                    height={100}
                    alt="doctor"
                    className="size-6"
                  />
                  <p className="whitespace-nowrap">
                    Dr. {appointment.doctor.name}
                  </p>
                </div>
                <div className="flex gap-2">
                  <Image
                    src="/icons/calendar.svg"
                    width={24}
                    height={24}
                    alt="calendar"
                  />
                  <p>{formatDateTime(appointment.schedule)}</p>
                </div>
              </>
            )
          )}
        </section>

        <Button variant="outline" className="shad-primary-btn" asChild>
          <Link href={`/patients/${params.userId}/new-appointment`}>
            Create New Appointment
          </Link>
        </Button>

        <div className="text-14-regular flex justify-between">
          <div>
            <p className="copyright">&copy; 2024 CareCoordinator</p>
            <Link href="https://www.flaticon.com/free-icons/healthcare-and-medical">
              <p className={cn("copyright", "!text-xs mt-2 !text-center")}>
                Logo icon by{" "}
                <span className="underline hover:opacity-80 transition-all">
                  Flaticon
                </span>
              </p>
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
};

export default Success;
