import { OptiSigns } from "@optisigns/optisigns";

export async function unpairDevice(
  apiKey: string,
  deviceId: string,
  teamId: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const result = await client.devices.unpairDevice(deviceId, teamId);
    return result;
  } catch (error: any) {
    throw new Error(`Failed to unpair device: ${error.message}`);
  }
}
