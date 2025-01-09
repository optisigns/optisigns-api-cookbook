import { OptiSigns } from "@optisigns/optisigns";

export async function moveDeviceToFolder(
  apiKey: string,
  deviceId: string,
  folderPath: string,
  teamId: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const updatedDevice = await client.devices.moveDeviceToFolder(
      deviceId,
      folderPath,
      teamId
    );
    return updatedDevice;
  } catch (error: any) {
    throw new Error(`Failed to move device to folder: ${error.message}`);
  }
}
