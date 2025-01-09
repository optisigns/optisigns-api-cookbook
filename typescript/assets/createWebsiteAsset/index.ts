import { OptiSigns } from "@optisigns/optisigns";

/**
 * Creates a new Website App Asset in OptiSigns.
 * @param apiKey - Your OptiSigns API key
 * @param url - The website URL
 * @param title - Display title for the website asset
 * @param teamId - The team ID to associate the asset with
 * @returns The newly created Asset object
 */
export async function createWebsiteAppAsset(
  apiKey: string,
  url: string,
  title: string,
  teamId: string
) {
  try {
    const client = new OptiSigns(apiKey);
    const newAsset = await client.assets.createWebsiteAppAsset(
      { url, title },
      teamId
    );
    return newAsset;
  } catch (error: any) {
    throw new Error(`Failed to create Website App Asset: ${error.message}`);
  }
}
