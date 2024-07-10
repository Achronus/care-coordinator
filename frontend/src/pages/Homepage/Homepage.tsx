import PatientForm from "@/forms/PatientForm";
import Image from "next/image";
import Link from "next/link";

type Props = {};

const Homepage = ({}: Props) => {
  return (
    <main className="flex h-screen max-h-screen">
      {/* TODO: OTP Verification */}

      <section className="remove-scrollbar container my-auto">
        <div className="sub-container max-w-[496px]">
          <Image
            src="/logo.svg"
            height={1000}
            width={1000}
            alt="Logo"
            className="mb-12 h-12"
          />

          <PatientForm />

          <div className="text-14-regular mt-20 flex justify-between">
            <p className="copyright">&copy; 2024 CareCoordinator</p>
            <Link href="/?admin=true" className="text-green-500">
              Admin
            </Link>
          </div>
        </div>
      </section>

      <Image
        src="/onboarding.png"
        height={1000}
        width={1000}
        alt="Onboarding"
        className="side-img max-w-[55%]"
      />
    </main>
  );
};

export default Homepage;
