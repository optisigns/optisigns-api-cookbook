import { OptiSigns } from "@optisigns/optisigns";

export async function pairDevice(
  apiKey: string,
  pairingCode: string,
  path: string,
  teamId: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const newDevice = await client.devices.pairDevice(
      pairingCode,
      path,
      teamId
    );
    return newDevice;
  } catch (error: any) {
    throw new Error(`Failed to pair device: ${error.message}`);
  }
}
