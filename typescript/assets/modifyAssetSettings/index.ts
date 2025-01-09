import { OptiSigns } from "@optisigns/optisigns";
import { AssetInput } from "@optisigns/optisigns/dist/types/asset";

/**
 * Modifies settings for an existing Asset.
 * This function delegates to either file-type or website-type modifications inside the SDK.
 * @param apiKey - Your OptiSigns API key
 * @param assetId - The unique ID of the Asset to update
 * @param settings - A partial set of settings to update
 * @param teamId - (Optional) The team ID for authorization
 * @returns The updated Asset object
 */
export async function modifyAssetSettings(
  apiKey: string,
  assetId: string,
  settings: Partial<AssetInput>,
  teamId?: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const updatedAsset = await client.assets.modifyAssetSettings(
      assetId,
      settings,
      teamId
    );
    return updatedAsset;
  } catch (error: any) {
    throw new Error(`Failed to modify asset settings: ${error.message}`);
  }
}
