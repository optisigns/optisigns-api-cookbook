import { OptiSigns } from "@optisigns/optisigns";

export async function updateContentTagRule(
  apiKey: string,
  deviceId: string,
  contentTagRuleId: string,
  teamId: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const updatedDevice = await client.devices.updateContentTagRule(
      deviceId,
      contentTagRuleId,
      teamId
    );
    return updatedDevice;
  } catch (error: any) {
    throw new Error(`Failed to update content tag rule: ${error.message}`);
  }
}
