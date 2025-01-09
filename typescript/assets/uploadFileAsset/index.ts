import { OptiSigns } from "@optisigns/optisigns";

/**
 * Uploads a file asset (e.g., images, videos, PDFs) to OptiSigns.
 * @param apiKey - Your OptiSigns API key
 * @param filePath - Local file path or a remote URL
 * @param fileName - The desired name for the file asset
 * @param teamId - ID of the team to associate the asset with (default: "1")
 * @returns The newly created Asset object
 * @throws An error if the upload fails
 */
export async function uploadFileAsset(
  apiKey: string,
  filePath: string,
  fileName: string,
  teamId: string = "1"
) {
  try {
    const client = new OptiSigns(apiKey);
    // Directly call our Assets SDK function
    const newAsset = await client.assets.uploadFileAsset(
      filePath,
      fileName,
      teamId
    );
    return newAsset;
  } catch (error: any) {
    throw new Error(`Failed to upload file asset: ${error.message}`);
  }
}
