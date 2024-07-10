<h1>Keyword-Select-Service</h1>

<h2>ROS2 service written in Python to extract keywords from transcribed text, send them to the server, and for the server to broadcast them.</h2>

<p>This repository consists of two ROS2 packages, <b>listener and serv</b>.</p>
<p>Listener consists of the client that extracts the actual keywords from the transcribed text, then asynchronously sends them to the server</p>
<p>Serv consists of the server that receives the keywords and broadcasts them to the command line.</p>
<p>These ROS2 packages are meant to work with https://github.com/realaryann/input_saver (speech-to-text converter)</p>

<h3>Installation</h3>
<ul>
  <li>Download the <b>listener and serv</b> packages into your {ros2 workspace}/src</li>
  <li>Execute <b>colcon build</b> in the workspace root</li>
  <li>Execute <b>source install/setup.bash</b> to source essential files</li>
</ul>

<h3>Adding Keywords</h3>
<ul>
  <li>Navigate to listener/dict</li>
  <li>Open dict.yaml and add any keywords you wish to detect</li>
</ul>

<h3>Reading the text</h3>
<ul>
  <li>PATHs for this service are absolute and <b>need to be changed</b> to correctly read the text</li>
  <li>You can change the path of the input file by navigating to listener/listener and replace any PATHs leading to test.txt</li>
</ul>

<h3>Running the service</h3>
<ul>
  <li>Open two terminals, three if you wish for live transcription to broadcasting</li>
  <li>Navigate to your ROS2 workspace</li>
  <li>In terminal 1, execute <b>ros2 run serv key_listen</b></li>
  <li>In terminal 2, execute <b>ros2 run listener key_node</b></li>
  <li>In terminal 3, navigate to your input_saver and run <b>sudo ./input.sh</b></li>
  <li>Record any audio with the specified keywords in it and observe the keywords broadcasted to the server!</li>
</ul>
