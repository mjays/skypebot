# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

## Copypaste this example command to create new scratch commands
## Leave this one alone so new commands can be made from it.
## Also: Please indent using spaces.
class ExampleCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("lobs a dolphin at $name.") ]
        self.command_mappings = [ "w3t", "splashy" ]
        self.enabled = False # change to True (or just delete this line) to enable a command

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

                
class GangnamCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "gangnam" ]
        self.templates = [  Template("(lalala)"),
                            Template("(tmi)"),
                            Template("(\o/)")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
class TrialCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "trial" ]
        self.templates = [  Template("asks $name to leave, never to return."),
                            Template("thinks that it's OK for $name to stay a little while longer."),
                            Template("doesn't like Kafka."),
                            Template("gets the bouncers onto $name."),
                            Template("calls his Mafia mates."),
                            Template("has rigged the jury against $name."),
                            Template("makes $name a straw man."),
                            Template("is wearing a wig."),
                            Template("dozed off."),
                            Template("bonks $name on the head with his gavel."),
                            Template("thinks Facebook is a more suitable environ for $name."),
                            Template("asks $name to bugger off to LambdaMOO."),
                            Template("is involved in a bit of extraordinary rendition of $name."),
                            Template("invades the Ecuadorian embassy to extradite $name."),
                            Template("gives $name a perminent Phactory Bar green card.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out     
        
        
class ChickenTownCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "chickentown" ]
        self.templates = [  Template("says the fucking beer is fucking fucked"),
                            Template("knows the fucking crisps are fucking old"),
                            Template("wants the fucking punters off his fucking back"),
                            Template("smells the fucking dope in the fucking bogs"),
                            Template("pours a fucking !drink for the fucking lads"),                                
                            Template("mops the fucking floor with a fucking mop"),
                            Template("cleans the fucking glasses with some fucking water"),
                            Template("flicks some fucking peanuts in $name’s fucking glass"),
                            Template("plays some fucking darts with the fucking some fucking darts"),
                            Template("serves a fucking !snack to the fucking law")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out 
        
        
        
class ShootoutCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "shootout" ]
        self.templates = [  Template("does gun fingers at $name."),
                            Template("makes a machine gun noise with his mouth."),
                            Template("turns around in slow motion."),
                            Template("reloads."),
                            Template("blows the smoke away from his invisible barrel."),
                            Template("spins his pretend revolver."),
                            Template("adjusts his ten-gallon hat."),
                            Template("holsters his pistol.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class AnusCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "anus" ]
        self.templates = [  Template("(moon)"),
                            Template("goes all yadda yadda yadda"),
                            Template("looks at a picture of !satan")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
        
class HoyleCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "hoyle", "atom", "atomoil" ]
        self.templates = [  Template("gets a bit ranty."),
                            Template("does a !satan on !satan."),
                            Template("causes trouble."),
                            Template("twiddles knobs.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        

class PeterCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "peter", "pit", "bihr" ]
        self.templates = [  Template("invites $name to a conference."),
                            Template("has hours of panels to fill."),
                            Template("assembles the band"),
                            Template("gets the bar into SXSW."),
                            Template("fires up his !prezi"),
                            Template("goes solo")                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out


class GoonCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "goon", "bouncer" ]
        self.templates = [  Template("leans on $name."),
                            Template("kneecaps $name."),
                            Template("asks $name to take a seat."),
                            Template("cracks his knuckles."),
                            Template("flashes a toothless grin at $name."),
                            Template("doesn't have a neck."),
                            Template("rotates his head, crunching his bones."),
                            Template("is wearing a donkey jacket."),
                            Template("tells $name to behave."),
                            Template("emails $name a toe."),
                            Template("can't be bought."),
                            Template("is selling DVD-players round the back of the pub."),
                            Template("thinks $name wants to 'ave a bit of fun."),
                            Template("posts a naked picture of $name to their family."),
                            Template("knows a thing or two about $name."),
                            Template("peels an orange, very bloody slowly."),
                            Template("bundles $name into the boot of his Vauxhall."),
                            Template("has a picture of $name's family."),
                            Template("thinks $name has a nice place here. Be a shame if anything happened to it."),
                            Template("suggests that $name should know what's good for them."),
                            Template("mutters something vaguely menacing in a gravelly voice to $name.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class LoonCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "loon", "mad" ]
        self.templates = [  Template("wears a foil !hat."),
                            Template("has mercury poisoning."),
                            Template("believes David Icke."),
                            Template("talks to himself."),
                            Template("hasn't washed for weeks."),
                            Template("doesn't trust the barge folk."),
                            Template("has all his money in carrier bags under the bed."),
                            Template("is concerned about all the lizards."),
                            Template("is carrying a copy of Catcher In The Rye."),
                            Template("cuts out bits of newspapers for his scrapbooks."),
                            Template("is still listening to !gangnam."),
                            Template("is late for a !tea party."),
                            Template("thinks $name has stolen his thoughts."),
                            Template("is called Bobbin. Are you my mother?")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class MynewCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "mynew", "new" ]
        self.templates = [  Template("understands that $name's new $startup is called $word.") ]
        self.startup = [ "startup",
            "product",
            "habit",
            "position",
            "desire",
            "beau" ]

        self.word = [ "Social Media Narcissism",
            "Guru Zentrum",
            "Corporate Density",
            "Spatial Complexity",
            "Loving Spoonful",
            "Braun Zucker",
            "Algorithmic Data Massage",
            "New Aesthetic Fashion",
            "Financial Jiu Jitsu",
            "Culture Jam",
            "Cube Farm",
            "Beanbag Office",
            "Stress Puppy",
            "Food Stamps",
            "Seagull Management",
            "Ninja Central",
            "Handsome Adult",
            "Bereaved Objects",
            "Absolute Nothingness",
            "Pipe Bomb",
            "True Say",
            "Handspeed Record",
            "Stealth Made",
            "Broken Windows",
            "Engagement Metrics",
            "Barry",
            "Piss und Shit",
            "Blended Synergy",
            "Billy Cosby Sweater Design" ]

    def generate( self, name ):
        startup = random.choice( self.startup )
        word = random.choice( self.word )
        template = random.choice( self.templates )
        message_out = template.substitute(name=name, startup=startup, word=word)
        return "/me %s" % message_out
    

