import FormLayout from "@/layouts/Form";
import { Logo, RegisterImg } from "@/lib/constants";

const Registration = () => {
  return (
    <main className="flex h-screen max-h-screen">
      <FormLayout
        containerStyles="max-w-[860px] flex-1 flex-col py-10"
        logo={Logo}
        displayImg={RegisterImg}
      >
        {/* <PatientForm /> */}
      </FormLayout>
    </main>
  );
};

export default Registration;

// 1:21:55
