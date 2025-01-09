# deleteAssetById

Deletes an existing Asset by its ID from OptiSigns.

## Example Usage

```ts
import { deleteAssetById } from "./deleteAssetById";

async function example() {
  try {
    const wasDeleted = await deleteAssetById(
      "YOUR_API_KEY",
      "ASSET_ID",
      "TEAM_ID"
    );
    console.log("Asset successfully deleted?", wasDeleted);
  } catch (error) {
    console.error(error);
  }
}
```
