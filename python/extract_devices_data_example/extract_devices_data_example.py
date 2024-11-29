import json
import requests
import os
import csv

# URLs for GraphQL server and file upload API
graphql_url = "https://graphql-gateway.optisigns.com/graphql"

# Retrieve API key from the environment variable
api_key = os.getenv("OPTISIGNS_API_KEY")  # Use OPTISIGNS_API_KEY from the environment

if not api_key:
    raise ValueError("Environment variable OPTISIGNS_API_KEY is not set.")

def graphql_request(query):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(graphql_url, json=query, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed with status code {response.status_code}: {response.text}")

def extract_devices_data():
    graphql_query = {
        "query": """
        query {
            devices(query: {}) {
                page {
                    edges {
                        cursor,
                        node {
                            UUID,
                            _id,
                            accountId,
                            activationDate,
                            aiVersion,
                            assignItem {
                                key
                                value
                            },
                            backgroundAWSS3ID,
                            backgroundAssetId,
                            backgroundBucket,
                            backgroundColor,
                            backgroundType,
                            createdAt,
                            createdBy,
                            creationDate,
                            currentAssetId,
                            currentPlaylistId,
                            currentScheduleId,
                            currentSelectionDate,
                            currentType,
                            device,
                            deviceName,
                            documentDuration,
                            feature,
                            featureData,
                            flashAssetId,
                            groupId,
                            heartbeatInterval,
                            isVirtual,
                            isWebViewer,
                            lastHeartBeat,
                            lastTeamId,
                            lastUpdatedBy,
                            lastUpdatedDate,
                            localAppVersion,
                            manufacturer,
                            model,
                            name,
                            orientation,
                            os,
                            osVersion,
                            pairingCode,
                            path,
                            platform,
                            pollingInterval,
                            sendData,
                            status,
                            statusContent,
                            stretchAsset,
                            syncPlay,
                            tags,
                            teamId,
                            totalStorage,
                            usedStorage,
                            videoPlayerType
                        }
                    }
                }
            }
        }
        """
    }

    resp = graphql_request(graphql_query)
    if resp:
        devices = resp.get("data", {}).get("devices", {}).get("page", {}).get("edges", [])
        with open("devices_data_extract.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow([
                "UUID", "_id", "accountId", "activationDate", "aiVersion", "assignItem", "backgroundAWSS3ID",
                "backgroundAssetId", "backgroundBucket", "backgroundColor", "backgroundType", "createdAt",
                "createdBy", "creationDate", "currentAssetId", "currentPlaylistId", "currentScheduleId",
                "currentSelectionDate", "currentType", "device", "deviceName", "documentDuration", "feature",
                "featureData", "flashAssetId", "groupId", "heartbeatInterval", "isVirtual", "isWebViewer",
                "lastHeartBeat", "lastTeamId", "lastUpdatedBy", "lastUpdatedDate", "localAppVersion", "manufacturer",
                "model", "name", "orientation", "os", "osVersion", "pairingCode", "path", "platform",
                "pollingInterval", "sendData", "status", "statusContent", "stretchAsset", "syncPlay", "tags",
                "teamId", "totalStorage", "usedStorage", "videoPlayerType"
            ])
            # Write the device data
            for device in devices:
                node = device.get("node", {})
                writer.writerow([
                    node.get("UUID", ""), node.get("_id", ""), node.get("accountId", ""), node.get("activationDate", ""),
                    node.get("aiVersion", ""), json.dumps(node.get("assignItem", {})), node.get("backgroundAWSS3ID", ""),
                    node.get("backgroundAssetId", ""), node.get("backgroundBucket", ""), node.get("backgroundColor", ""),
                    node.get("backgroundType", ""), node.get("createdAt", ""), node.get("createdBy", ""),
                    node.get("creationDate", ""), node.get("currentAssetId", ""), node.get("currentPlaylistId", ""),
                    node.get("currentScheduleId", ""), node.get("currentSelectionDate", ""), node.get("currentType", ""),
                    node.get("device", ""), node.get("deviceName", ""), node.get("documentDuration", ""),
                    json.dumps(node.get("feature", {})), json.dumps(node.get("featureData", {})), node.get("flashAssetId", ""),
                    node.get("groupId", ""), node.get("heartbeatInterval", ""), node.get("isVirtual", ""),
                    node.get("isWebViewer", ""), node.get("lastHeartBeat", ""), node.get("lastTeamId", ""),
                    node.get("lastUpdatedBy", ""), node.get("lastUpdatedDate", ""), node.get("localAppVersion", ""),
                    node.get("manufacturer", ""), node.get("model", ""), node.get("name", ""), node.get("orientation", ""),
                    node.get("os", ""), node.get("osVersion", ""), node.get("pairingCode", ""), node.get("path", ""),
                    node.get("platform", ""), node.get("pollingInterval", ""), node.get("sendData", ""),
                    node.get("status", ""), node.get("statusContent", ""), node.get("stretchAsset", ""),
                    node.get("syncPlay", ""), json.dumps(node.get("tags", [])), node.get("teamId", ""), node.get("totalStorage", ""),
                    node.get("usedStorage", ""), node.get("videoPlayerType", "")
                ])

if __name__ == "__main__":
    extract_devices_data()