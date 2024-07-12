import PatientForm from "@/forms/PatientForm";
import FormLayout from "@/layouts/Form";
import { DisplayImg, Logo } from "@/lib/constants";

type Props = {};

const Homepage = ({}: Props) => {
  return (
    <main className="flex h-screen max-h-screen">
      {/* TODO: OTP Verification */}
      <FormLayout
        containerStyles="max-w-[496px]"
        logo={Logo}
        displayImg={DisplayImg}
      >
        <PatientForm />
      </FormLayout>
    </main>
  );
};

export default Homepage;
