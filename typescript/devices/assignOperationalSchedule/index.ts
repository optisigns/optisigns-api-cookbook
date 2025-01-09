import { OptiSigns } from "@optisigns/optisigns";

export async function assignOperationalSchedule(
  apiKey: string,
  deviceId: string,
  scheduleOpsId: string,
  teamId: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const updatedDevice = await client.devices.assignOperationalSchedule(
      deviceId,
      scheduleOpsId,
      teamId
    );
    return updatedDevice;
  } catch (error: any) {
    throw new Error(`Failed to assign operational schedule: ${error.message}`);
  }
}
