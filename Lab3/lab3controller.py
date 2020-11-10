# Lab 3 Skeleton
#
# Based on of_tutorial by James McCauley

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_firewall (self, packet, packet_in, port):
    # The code in here will be executed for every packet.
    #---------------------------------------------------------------------------------------------
    if packet.find('tcp'):
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet, port)
      msg.idle_timeout = 10
      msg.hard_timeout = 30
      msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
      msg.data = packet_in
      msg.priority = 44
      self.connection.send(msg)
      return
    elif packet.type == packet.ARP_TYPE:
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet, port)
      msg.idle_timeout = 10
      msg.hard_timeout = 30
      msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
      msg.data = packet_in
      msg.priority = 43
      self.connection.send(msg)
      return
    else:
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet, port)
      msg.idle_timeout = 10
      msg.hard_timeout = 30
      msg.data = packet_in
      msg.priority = 42
      self.connection.send(msg)
      """
      msg = of.ofp_packet_out()
      msg.buffer_id = packet_in.buffer_id
      msg.in_port = port
      msg.priority = 42
      self.connection.send(msg)
      """
      return

    #-------------------------------------------------------------------------------------------
  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_firewall(packet, packet_in, event.port)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
