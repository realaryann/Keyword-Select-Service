<h1>Keyword-Select-Service</h1>

<h2>ROS2 service written in Python to extract keywords from transcribed text, send them to the server, and for the server to broadcast them.</h2>

<p>This repository consists of two ROS2 packages, <b>listener and hubo_voice_command</b>.</p>
<p>Listener consists of the general client that extracts the actual keywords from the transcribed text, then asynchronously sends them to the server</p>
<p>hubo_voice_command consists of the server and action client that receives the keywords and deals with them individually by passing them off to the action server.</p>
<p>These ROS2 packages are meant to work with https://github.com/realaryann/input_saver (speech-to-text converter)</p>
<p>The custom service String is created to be used with these packages for transfer of keywords</p>
<p>custom action message Huboaction is created to be used to communicate to the action server</p>

<h3>Installation</h3>
<ul>
  <li>Download the  packages into your {ros2 workspace}/src</li>
  <li>Change the absolute paths in all files based on your file structure</li>
  <li>Execute <b>colcon build</b> in the workspace root</li>
  <li>Execute <b>source install/setup.bash</b> to source essential files</li>
</ul>

<h3>Adding Keywords</h3>
<ul>
  <li>Navigate to hubo_voice_command/dict</li>
  <li>Open hubo_dict.yaml and add any keywords you wish to detect</li>
  <li>If working with other robots, you must declare their yaml dictionaries in this directory</li>
</ul>

<h3>Working with other Robots</h3>
<ul>
  <li>If working with a different robot, you must create a different service provider for the robot, but the client can stay the same!</li>
  <li>To create a different service provider, you can do so by creating a different package and linking the service provider to 'key_listen'</li>
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
  <li>In terminal 1, execute <b>ros2 run hubo_voice_command key_listen</b></li>
  <li>In terminal 2, execute <b>ros2 launch hubo_voice_node.launch.py</b></li>
  <li>In terminal 3, navigate to your input_saver and run <b>./input.sh</b></li>
  <li>Record any audio with the specified keywords in it and observe the keywords broadcasted to the server!</li>
</ul>
