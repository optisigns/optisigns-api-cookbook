import { OptiSigns } from "@optisigns/optisigns";

export async function getDeviceById(apiKey: string, deviceId: string) {
  try {
    const client = new OptiSigns(apiKey);
    const device = await client.devices.getDeviceById(deviceId);
    return device;
  } catch (error: any) {
    throw new Error(`Failed to get device by ID: ${error.message}`);
  }
}
