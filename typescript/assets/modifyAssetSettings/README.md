# modifyAssetSettings

Modifies settings on an existing Asset in OptiSigns (both file-type and website-type assets).

## Example Usage

```ts
import { modifyAssetSettings } from "./modifyAssetSettings";

async function example() {
  try {
    const updatedAsset = await modifyAssetSettings(
      "YOUR_API_KEY",
      "ASSET_ID",
      {
        name: "Updated Asset Name",
        path: "/New/Folder",
        // ...other fields from the AssetInput type
      },
      "TEAM_ID"
    );
    console.log("Updated Asset:", updatedAsset);
  } catch (error) {
    console.error(error);
  }
}
```
