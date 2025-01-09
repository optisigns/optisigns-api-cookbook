# uploadFileAsset

Uploads a file (local or remote) as a new Asset in OptiSigns.

## Example Usage

```ts
import { uploadFileAsset } from "./uploadFileAsset";

async function example() {
  try {
    const newAsset = await uploadFileAsset(
      "YOUR_API_KEY",
      "/path/to/local-or-remote-file.png",
      "MyCoolImage.png",
      "TEAM_ID"
    );
    console.log("Uploaded Asset:", newAsset);
  } catch (error) {
    console.error(error);
  }
}
```
