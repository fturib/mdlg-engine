<p>files in <b>{{folder}}</b>
<ul>
    %for file in files:
    <li><a href="{{file['query']}}">{{file['name']}}</a>  -- <a href="{{file['query']}}?download=true">Download</a></li>
    %end
</ul>

<p>subdirs in <b>{{folder}}</b>
<ul>
    %for dir in dirs:
    <li><a href="{{dir['query']}}">{{dir['name']}}</a></li>
    %end
</ul>


<p><a href="/help">Back to help and available commands</a></p>