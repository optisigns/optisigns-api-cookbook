# createWebsiteAppAsset

Creates a "Website" type of Asset in OptiSigns (e.g., to load a webpage).

## Example Usage

```ts
import { createWebsiteAppAsset } from "./createWebsiteAppAsset";

async function example() {
  try {
    const newWebAsset = await createWebsiteAppAsset(
      "YOUR_API_KEY",
      "https://www.example.com",
      "My Awesome Website",
      "TEAM_ID"
    );
    console.log("New Website Asset:", newWebAsset);
  } catch (error) {
    console.error(error);
  }
}
```
