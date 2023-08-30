"""ProgressOpenEdge tap class."""

from __future__ import annotations

from singer_sdk import SQLTap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_progressopenedge.client import ProgressOpenEdgeStream


class TapProgressOpenEdge(SQLTap):
    """ProgressOpenEdge tap class."""

    name = "tap-progressopenedge"
    default_stream_class = ProgressOpenEdgeStream

    config_jsonschema = th.PropertiesList(
        th.Property("Driver", th.StringType, required=True, description="The specified driver"),              
        th.Property("Host", th.StringType, required=True, description="The host to establish connection with."),       
        th.Property("Port",th.StringType,required=True,description="The port number."),        
        th.Property("Database",th.StringType,required=True,description="The database to establish connection with."),        
        th.Property("User",th.StringType,required=True,description="The user field."),
        th.Property("Password",th.StringType,required=True,secret=True,description="The password field."),
    ).to_dict()


if __name__ == "__main__":
    TapProgressOpenEdge.cli()
