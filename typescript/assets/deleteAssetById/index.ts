import { OptiSigns } from "@optisigns/optisigns";

/**
 * Permanently deletes an Asset by its ID.
 * @param apiKey - Your OptiSigns API key
 * @param assetId - The ID of the Asset to delete
 * @param teamId - The ID of the team that owns the Asset
 * @returns Boolean indicating whether the deletion succeeded
 */
export async function deleteAssetById(
  apiKey: string,
  assetId: string,
  teamId: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const result = await client.assets.deleteAssetById(assetId, teamId);
    return result;
  } catch (error: any) {
    throw new Error(`Failed to delete asset: ${error.message}`);
  }
}
