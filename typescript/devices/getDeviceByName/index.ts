import { OptiSigns } from "@optisigns/optisigns";

export async function getDeviceByName(apiKey: string, name: string) {
  try {
    const client = new OptiSigns(apiKey);
    const matchingDevices = await client.devices.getDeviceByName(name);
    return matchingDevices;
  } catch (error: any) {
    throw new Error(`Failed to get device by name: ${error.message}`);
  }
}
