from debtcollector import moves
import warnings 

class UseDebtcollector(object) :
    """
    https://docs.openstack.org/debtcollector/latest/user/index.html
    
    A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner. The goal of this library is to provide well documented developer facing deprecation patterns that start of with a basic set and can expand into a larger set of patterns as time goes on. The desired output of these patterns is to apply the warnings module to emit DeprecationWarning or PendingDeprecationWarning or similar derivative to developers using libraries (or potentially applications) about future deprecations.
    """

    @moves.moved_method("trun", version="1.1")
    def trun_left(self):
        """
        .. deprecated:: 1.1
        """

        warnings.warn("trun_left is deprecated, use turn instead",
                     DeprecationWarning)
        pass

    def trun(self, direction="left") :
        pass

    