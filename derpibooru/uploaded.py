# Copyright (c) 2014, Joshua Stone
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from .user import User

class Uploaded(User):
  """
  This is the base class in which other classes centered around user data will
  inherit since their URL parameters so similar
  """
  def __init__(self, key, page=1, perpage=15, comments=False, fav=False):
    User.__init__(self, key, page, perpage, comments, fav)

  @property
  def url(self):
    url, parameters = self.hostname + "/images/uploaded.json", []

    parameters.append("key={0}".format(self.key))
    parameters.append("perpage={0}".format(self.perpage))
    parameters.append("page={0}".format(self.page))

    if self.comments == True:
      parameters.append("comments=")
    if self.fav == True:
      parameters.append("fav=")

    url += "?{0}".format("&".join(parameters))

    return(url)

  @property
  def random(self):
    url = self.hostname + "/images/uploaded.json?random=y&key=" + self.key

    return(url)
