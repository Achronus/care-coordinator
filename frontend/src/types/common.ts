type ImageType = {
  src: string;
  alt: string;
  className?: string;
  width?: number;
  height?: number;
};

type Doctor = {
  name: string;
  avatarIcon: string;
  id: string;
};

type AppointmentDetails = {
  type: string;
  status: string;
  iconUrl: string;
};
