export type ImageType = {
  src: string;
  alt: string;
  className?: string;
  width?: number;
  height?: number;
};

export type Doctor = {
  name: string;
  avatarIcon: string;
  id: string;
};

export type AppointmentDetails = {
  type: string;
  status: string;
  iconUrl: string;
};

export type StatCardTypes = "create" | "cancel" | "schedule";
