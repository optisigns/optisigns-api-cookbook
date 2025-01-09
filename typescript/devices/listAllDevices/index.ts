import { OptiSigns } from "@optisigns/optisigns";

export async function listAllDevices(apiKey: string) {
  try {
    // Instantiate the SDK client with your API key
    const client = new OptiSigns(apiKey);

    // Call the built-in function from the "devices" module
    const devices = await client.devices.listAllDevices();

    return devices;
  } catch (error: any) {
    throw new Error(`Failed to list all devices: ${error.message}`);
  }
}
