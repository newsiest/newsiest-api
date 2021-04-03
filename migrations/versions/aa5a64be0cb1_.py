"""empty message

Revision ID: aa5a64be0cb1
Revises: 
Create Date: 2021-03-25 20:41:36.787257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa5a64be0cb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('author2', sa.String(), nullable=True), schema='news')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'author2', schema='news')
    # ### end Alembic commands ###