<p>HELLO - Help for Mdlg Engine web service</p>

<ul>
Available routes are:
<li><a href="/help"><b>/help</b></a> - this tiny help page</li>
<li><a href="/hello"><b>/hello</b></a> - verify the server is up by calling the hello world</li>
<li><a href="/run/demo"><b>/run/demo</b></a> run the provided demo samples</li>
<li><b>/run/[sub-dir-path]</b> run your own training/prediction for the demo process located in /data/[sub-dir-path]</li>
<li><a href="/files"><b>/files</b></a>list files of the mounted share disk (data of the demos)
<li><b>/files/[any-path]</b>list files of the dir [any-path] of the mounted share disk (data of the demos)
</ul>

NOTE: All shared data is in the container's folder : /data.